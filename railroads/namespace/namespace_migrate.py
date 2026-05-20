import cairosvg
from railroad import *

MIGRATE_UNIT_TEST = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('migrate'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('unit-test'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-export-path'), '{export-path}'),
                                Sequence(NonTerminal('-specs-path'), '{specs-path}')
                            )
                        )
                    )
                )
            )
        )
    )
)

MIGRATE_UNIT_TEST_MANUAL = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('migrate'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('unit-test-manual'),
                    Choice(0, 
                        Terminal('help'),
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
                                Sequence(NonTerminal('-proect-id'), '{project-id}')
                            )
                        )
                    )
                )
            )
        )
    )
)

migrate = {
    'migrate-unit-test': MIGRATE_UNIT_TEST,
    'migrate-unit-test-manual': MIGRATE_UNIT_TEST_MANUAL
}
