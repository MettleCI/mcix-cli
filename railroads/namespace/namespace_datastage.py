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


DATASTAGE_CAPTURE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('capture'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-location'), '{directory}'),
                                Sequence(NonTerminal('-project-cache'), '{directory}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-threads'), '{number}')
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_CCMT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('ccmt'), 
                                        Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-logfile'), '{filename}'),
                                Sequence(NonTerminal('-isxdirectory'), '{directory}'),
                            ),
                            Optional(
                                Choice(0, 
                                    Sequence(NonTerminal('-param'), '{parameter}'),
                                    Sequence(NonTerminal('-project-cache'), '{directory}'),
                                    Sequence(NonTerminal('-threads'), '{number}'),
                                    Sequence(NonTerminal('-heapsize'), '{number}'),
                                    Sequence(NonTerminal('-noBatchThreshold'), '{path}'),
                                ),
                                'skip'
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_CLEANUP_PROJECTS = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cleanup-projects'), 
                                        Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-pattern'), '{filename}'),
                            ),
                            Optional(
                                Choice(0, 
                                Sequence(NonTerminal('-retain'), '{number}'),
                                ),
                                'skip'
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_CREATE_PROJECT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('create-project'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-path'), '{path}')
                            )
                        )
                    )
                )
            )
        )
    )
)



DATASTAGE_DELETE_PROJECT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('delete-project'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_DEPLOY = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('deploy'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-assets'), '{directory}'),
                                Sequence(NonTerminal('-project-cache'), '{directory}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-include-job-in-test-name')), 
                                Sequence(NonTerminal('-threads'), '{number}'),
                                Sequence(NonTerminal('-parameter-sets'), '{directory}')
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_EXECUTE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('execute'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-jobname'), '{job}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-runmode'), 'NORMAL|RESET|RESTART|VALIDATE'),
                                Sequence(NonTerminal('-param'), '{parameter}')
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
    'datastage-export': DATASTAGE_EXPORT,
    'datastage-capture': DATASTAGE_CAPTURE,
    'datastage-ccmt': DATASTAGE_CCMT,
    'datastage-cleanup-projects': DATASTAGE_CLEANUP_PROJECTS,
    'datastage-create-project': DATASTAGE_CREATE_PROJECT,
    'datastage-delete-project': DATASTAGE_DELETE_PROJECT,
    'datastage-deploy': DATASTAGE_DEPLOY,
    'datastage-execute': DATASTAGE_EXECUTE
}