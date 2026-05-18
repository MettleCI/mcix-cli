import cairosvg
from railroad import *

FABRICATION_LIST = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('fabrication'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('list'), 
                    Choice(0,
                        'help',
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
            )
        )
    )
)

FABRICATION_TEST = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('fabrication'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('test'), 
                    Choice(0,
                        'help',
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
                            ),
                        )
                    )
                )
            )
        )
    )
)

fabrication = {
    'fabrication-list': FABRICATION_LIST,
    'fabrication-test': FABRICATION_TEST
}