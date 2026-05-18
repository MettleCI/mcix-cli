import cairosvg
from railroad import *

REMOTE_DOWNLOAD = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('remote'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('download'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(
                                    NonTerminal('-host'), '{host}',
                                    Optional(
                                        Sequence(NonTerminal('-port'), '{port}'),
                                    )
                                ),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-source'), '{path}'),

                                Sequence(NonTerminal('-transferPattern'), '{transferPattern}'),
                            ),
                            Optional(
                                Sequence(NonTerminal('-destination'), '{path}'),
                            ),
                            Choice(0, 
                                Sequence(NonTerminal('-password'), '{password}'),
                                MultipleChoice(0, 'all', 
                                    Sequence(NonTerminal('-privateKey'), '{key}'),
                                    Sequence(NonTerminal('-passphrase'), '{passphrase}')
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

REMOTE_EXECUTE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('remote'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('execute'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(
                                    NonTerminal('-host'), '{host}',
                                    Optional(
                                        Sequence(NonTerminal('-port'), '{port}'),
                                    )
                                ),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-script'), '{script}'),
                                Sequence(NonTerminal('-transferPattern'), '{transferPattern}'),
                            ),
                            Choice(0, 
                                Sequence(NonTerminal('-password'), '{password}'),
                                MultipleChoice(0, 'all', 
                                    Sequence(NonTerminal('-privateKey'), '{key}'),
                                    Sequence(NonTerminal('-passphrase'), '{passphrase}')
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

REMOTE_UPLOAD = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('remote'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('upload'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-host'), '{host}',
                                Choice(0,
                                    Sequence(Skip()),
                                    Sequence(NonTerminal('-port'), '{port}'),
                                    )
                                ),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-destination'), '{path}'),

                                Sequence(NonTerminal('-transferPattern'), '{transferPattern}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-source'), '{path}'),
                            ),
                            Choice(0, 
                                Sequence(NonTerminal('-password'), '{password}'),
                                MultipleChoice(0, 'all', 
                                    Sequence(NonTerminal('-privateKey'), '{key}'),
                                    Sequence(NonTerminal('-passphrase'), '{passphrase}')
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)


remote = {
    'remote-download': REMOTE_DOWNLOAD,
    'remote-execute': REMOTE_EXECUTE,
    'remote-upload': REMOTE_UPLOAD,
}