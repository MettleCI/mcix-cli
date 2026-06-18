import cairosvg
from railroad import *

OVERLAY_APPLY = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('overlay'),
            NonTerminal('apply')
        ),
        Sequence(
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-assets'), '{api-key}'),
                Sequence(NonTerminal('-output'), '{directory-or-filename}'),
                Sequence(NonTerminal('-overlay'), '{directory}')
            ),
            Choice(0,
                Sequence(NonTerminal('-properties'), '{filename}')
            )
        )
    )
)

datastage = {
    'overlay-apply': OVERLAY_APPLY
}