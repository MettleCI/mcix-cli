import cairosvg
from railroad import *

DATASTAGE_COMPILE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('compile'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-api-key'), '{api-key}'),
                                Sequence(NonTerminal('-url'), '{URL}'),
                                Sequence(NonTerminal('-user'), '{user}'),
                                Sequence(NonTerminal('-report'), '{filename}')
                            ),
                            Choice(0,
                                Sequence(NonTerminal('-project'), '{project-name}'),
                                Sequence(NonTerminal('-proect-id'), '{project-id}')
                            ),
                            Optional(
                                NonTerminal('-include-job-in-test-name')
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_IMPORT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('import'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-api-key'), '{api-key}'),
                                Sequence(NonTerminal('-url'), '{URL}'),
                                Sequence(NonTerminal('-user'), '{user}'),
                                Sequence(NonTerminal('-assets'), '{file-pattern}')
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


DATASTAGE_EXPORT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('export'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-api-key'), '{api-key}'),
                                Sequence(NonTerminal('-url'), '{URL}'),
                                Sequence(NonTerminal('-user'), '{user}'),
                                Sequence(NonTerminal('-export-path'), '{file-pattern}')
                            ),
                            Choice(0,
                                Sequence(NonTerminal('-project'), '{project-name}'),
                                Sequence(NonTerminal('-proect-id'), '{project-id}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-include-binaries'))
                            )
                        )
                    )
                )
            )
        )
    )
)

datastage = {
    'datastage-compile': DATASTAGE_COMPILE,
    'datastage-import': DATASTAGE_IMPORT,
    'datastage-export': DATASTAGE_EXPORT
}