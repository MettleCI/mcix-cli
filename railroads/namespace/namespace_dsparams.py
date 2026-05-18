import cairosvg
from railroad import *

DSPARAMS_DELETE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('delete'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-delete'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                            )
                        )
                    )
                )
            )
        )
    )
)

DSPARAMS_DIFF = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('diff'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                                Sequence(NonTerminal('-diff'), '{filename}')
                            )
                        )
                    )
                )
            )
        )
    )
)

DSPARAMS_MERGE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('merge'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-diff'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                            )
                        )
                    )
                )
            )
        )
    )
)

dsparams = {
    'dsparams-delete': DSPARAMS_DELETE,
    'dsparams-diff': DSPARAMS_DIFF,
    'dsparams-merge': DSPARAMS_MERGE
}