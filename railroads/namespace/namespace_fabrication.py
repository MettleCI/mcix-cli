import cairosvg
from railroad import *

FABRICATION_LIST = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('fabrication'),
            NonTerminal('list')
        ), 
        Sequence(
            Choice(0,
                Sequence(NonTerminal('-include-internal')),
                Sequence(NonTerminal('-path'), '{path}')
            ),
            Choice(0,
                Sequence(Skip()), 
                Sequence(NonTerminal('-include-params'))
            )
        )
    )
)

FABRICATION_TEST = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('fabrication'),
            NonTerminal('test')
        ),
        Sequence(
            MultipleChoice(0, 'all',
                Sequence(NonTerminal('-path'), '{path}'),
                Sequence("Generator", "{generator}"),
            ),
            MultipleChoice(0, 'any',
                Skip(), 
                Sequence(NonTerminal('-P'), '{param_name=param_value}')
            ),
            MultipleChoice(0, 'any',
                Skip(),
                Sequence(NonTerminal('-rowcount'), '{rows}'),
                Sequence(NonTerminal('-include-internal')),
            )
        )
    )
)

fabrication = {
    'fabrication-list': FABRICATION_LIST,
    'fabrication-test': FABRICATION_TEST
}