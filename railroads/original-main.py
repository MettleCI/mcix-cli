import cairosvg
from railroad import *

TRY_STATEMENT = Diagram(
    Terminal('try', 'skip'),
    Terminal(':'),
    NonTerminal('suite'),
    Choice(0,
           Sequence(
               OneOrMore(
                   Sequence(
                       Terminal('except'),
                       Optional(
                           Sequence(
                               NonTerminal('test'),
                               Optional(
                                   Sequence(
                                       Terminal('as'),
                                       NonTerminal('NAME')
                                   )
                               )
                           )
                       )
                   ), Arrow('<')
               ),
               Optional(
                   Sequence(
                       Terminal('else'),
                       Terminal(':'),
                       NonTerminal('suite')
                   )
               ),
               Optional(
                   Sequence(
                       Terminal('finally'),
                       Terminal(':'),
                       NonTerminal('suite')
                   )
               ),
           ),
           Sequence(
               Terminal('finally'),
               Terminal(':'),
               NonTerminal('suite')
           )
           )
)

WITH_STATEMENT = Diagram(
    Terminal('with', 'skip'),
    NonTerminal('test'),
    Optional(
        Sequence(
            Terminal('as'),
            NonTerminal('expr')
        )),
    Optional(OneOrMore(Sequence(
        Terminal(', as'),
        NonTerminal('expr')
    ), Arrow('<'))),
    Terminal(':'),
    NonTerminal('suite')
)


COMPLIANCE_QUERY = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('compliance'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('query'), 
                    Choice(0,
                        'help',
                            Sequence(
                                MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-queries'), '{location of query files}'),
                                Sequence(NonTerminal('-assets'), '{location of ISX assets}'),
                                Sequence(NonTerminal('-report'), '{CSV output report name}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-threads'), '{number of execution threads}')
                            )
                        )
                    )
                )
            )
        )
    )
)


statements = {
    'try-statement': TRY_STATEMENT,
    'with-statement': WITH_STATEMENT,
    'compliance-query': COMPLIANCE_QUERY
}


def main():
    for key, value in statements.items():
        with open('{0}.svg'.format(key), 'w') as out_svg:
            diagram = value
            diagram.writeSvg(out_svg.write)
        cairosvg.svg2png(url='{0}.svg'.format(key), write_to='{0}.png'.format(key), output_width=3000, dpi=300)


if __name__ == "__main__":
    main()
