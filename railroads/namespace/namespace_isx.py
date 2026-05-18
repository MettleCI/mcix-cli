import cairosvg
from railroad import *

ISX_CAT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cat'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                MultipleChoice(0, 'any',
                                    Sequence(NonTerminal('-pattern'), '{pattern}')
                                ),
                                Sequence(NonTerminal('-isx'), '{filename}')
                            ),
                            Choice(0,
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-fqDedupe')),
                            )
                        )
                    )
                )
            )
        )
    )
)

ISX_CUT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cut'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-dir'), '{directory}'),
                                Sequence(NonTerminal('-isx'), '{filename}')
                            )
                        )
                    )
                )
            )
        )
    )
)

ISX_EXPORT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('export'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{Services tier}'),
                                Sequence(NonTerminal('-server'), '{Engine tier}'),
                                Sequence(NonTerminal('-username'), '{User Name}'),
                                Sequence(NonTerminal('-password'), '{Password}'),
                                Sequence(NonTerminal('-project'), '{Project Name}')
                           ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-jobname'), '{Job specification}'),
                                Sequence(NonTerminal('-location'), '{Source directory}'),
                                Sequence(NonTerminal('-project-cache'), '{Cache directory}'),
                                Sequence(NonTerminal('-threads'), '{Thread count}'),
                                Sequence(NonTerminal('-include-binaries')),
                                Sequence(NonTerminal('-preview')),
                            )
                        )
                    )
                )
            )
        )
    )
)

ISX_IMPORT = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('import'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{Services tier}'),
                                Sequence(NonTerminal('-server'), '{Engine tier}'),
                                Sequence(NonTerminal('-username'), '{User Name}'),
                                Sequence(NonTerminal('-password'), '{Password}'),
                                Sequence(NonTerminal('-project'), '{Project Name}'),
                                Sequence(NonTerminal('-location'), '{Source directory}'),

                           ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-project-cache'), '{Cache directory}'),
                                Sequence(NonTerminal('-threads'), '{Thread count}'),
                                Sequence(NonTerminal('-parameter-sets'), '{Directory}'),
                                Sequence(NonTerminal('-exclude-designs')),
                                Sequence(NonTerminal('-whitelist')),
                            )
                        )
                    )
                )
            )
        )
    )
)

ISX_MESSAGE_HANDLERS = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('message-handlers'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-isx'), '{directory}'),
                                Sequence(NonTerminal('-msh'), '{directory}'),
                            )
                        )
                    )
                )
            )
        )
    )
)

ISX_SET_PARAMS = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('set-params'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'any',
                                Sequence(NonTerminal('-pattern'), '{File specification}')
                           ),
                            MultipleChoice(0, 'any',
                                Sequence(NonTerminal('-P'), '"{Variable}={Value}"'),

                            )
                        )
                    )
                )
            )
        )
    )
)

isx = {
    'isx_cat': ISX_CAT,
    'isx_cut': ISX_CUT,
    'isx_export': ISX_EXPORT,
    'isx_import': ISX_IMPORT,
    'isx_message_handlers': ISX_MESSAGE_HANDLERS,
    'isx_set_params': ISX_SET_PARAMS
 }