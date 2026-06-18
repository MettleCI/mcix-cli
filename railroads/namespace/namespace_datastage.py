import cairosvg
from railroad import *

DATASTAGE_COMPILE = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('datastage'),
            NonTerminal('compile')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-api-key'), '{api-key}'),
                Sequence(NonTerminal('-url'), '{URL}'),
                Sequence(NonTerminal('-user'), '{user}'),
                Sequence(NonTerminal('-report'), '{filename}')
            ),
            Choice(0,
                Sequence(NonTerminal('-project'), '{project-name}'),
                Sequence(NonTerminal('-project-id'), '{project-id}')
            ),
            Optional(
                NonTerminal('-include-job-in-test-name')
            )
        )
    )
)

DATASTAGE_EXPORT = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('datastage'),
            NonTerminal('export')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-api-key'), '{api-key}'),
                Sequence(NonTerminal('-url'), '{URL}'),
                Sequence(NonTerminal('-user'), '{user}'),
                Sequence(NonTerminal('-export-path'), '{file-pattern}')
            ),
            Choice(0,
                Sequence(NonTerminal('-project'), '{project-name}'),
                Sequence(NonTerminal('-project-id'), '{project-id}')
            ),
            MultipleChoice(0, 'any',
                Sequence(Skip()), 
                Sequence(NonTerminal('-include-binaries'))
            )
        )
    )
)

DATASTAGE_IMPORT = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('datastage'),
            NonTerminal('import')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-api-key'), '{api-key}'),
                Sequence(NonTerminal('-url'), '{URL}'),
                Sequence(NonTerminal('-user'), '{user}'),
                Sequence(NonTerminal('-assets'), '{file-pattern}')
            ),
            Choice(0,
                Sequence(NonTerminal('-project'), '{project-name}'),
                Sequence(NonTerminal('-project-id'), '{project-id}')
            )
        )
    )
)


datastage = {
    'datastage-compile': DATASTAGE_COMPILE,
    'datastage-import': DATASTAGE_IMPORT,
    'datastage-export': DATASTAGE_EXPORT
}