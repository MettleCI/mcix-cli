import cairosvg
from railroad import *

MIGRATE_UNIT_TEST = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('migrate'),
            NonTerminal('unit-test')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-export-path'), '{export-path}'),
                Sequence(NonTerminal('-specs-path'), '{specs-path}')
            )
        )
    )
)

MIGRATE_UNIT_TEST_MANUAL = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('migrate'),
            NonTerminal('unit-test-manual')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-api-key'), '{api-key}'),
                Sequence(NonTerminal('-url'), '{URL}'),
                Sequence(NonTerminal('-user'), '{user}'),
                Sequence(NonTerminal('-export-path'), '{export-path}'),
                Sequence(NonTerminal('-specs-path'), '{specs-path}')
            ),
            Choice(0,
                Sequence(NonTerminal('-project'), '{project-name}'),
                Sequence(NonTerminal('-project-id'), '{project-id}')
            )
        )
    )
)

migrate = {
    'migrate-unit-test': MIGRATE_UNIT_TEST,
    'migrate-unit-test-manual': MIGRATE_UNIT_TEST_MANUAL
}
