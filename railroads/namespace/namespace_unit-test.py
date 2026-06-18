import cairosvg
from railroad import *

UNIT_TEST_GENERATE = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('unit-test'),
            NonTerminal('generate')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-specs'), '{path}'),
                Sequence(NonTerminal('-assets'), '{path}')
            ),
            MultipleChoice(0, 'any',
                Sequence(Skip()),
                Sequence(NonTerminal('-joblist'), '{path}'),
                NonTerminal('-check-row-count-only'),
            )
        )
    )
)

UNIT_TEST_EXECUTE = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('unit-test'),
            NonTerminal('execute')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-domain'), '{domain}'),
                Sequence(NonTerminal('-server'), '{engine tier}'),
                Sequence(NonTerminal('-project'), '{project}'),
                Sequence(NonTerminal('-username'), '{user}'),
                Sequence(NonTerminal('-password'), '{password}'),
                Sequence(NonTerminal('-specs'), '{path}'),
                Sequence(NonTerminal('-reports'), '{path}'),
            ),
            MultipleChoice(0, 'any',
                Sequence(Skip()),
                Sequence(NonTerminal('-test-suite'), '{name}'),
                Sequence(NonTerminal('-threads'), '{threads}'),
                NonTerminal('-ignore-test-failures')
            )
        )
    )
)


unittest = { 
    'unit-test-generate': UNIT_TEST_GENERATE,
    'unit-test-execute': UNIT_TEST_EXECUTE
}