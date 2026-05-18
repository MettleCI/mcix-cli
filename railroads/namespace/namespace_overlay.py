import cairosvg
from railroad import *

OVERLAY_APPLY = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('overlay'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('apply'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-assets'), '{api-key}'),
                                Sequence(NonTerminal('-ouptut'), '{directory-or-filename}'),
                                Sequence(NonTerminal('-overlay'), '{directory}')
                            ),
                            Choice(0,
                                Sequence(NonTerminal('-properties'), '{filename}')
                            )
                        )
                    )
                )
            )
        )
    )
)


datastage = {
    'overlay-apply': OVERLAY_APPLY
}