import cairosvg
from railroad import *

SYSTEM_VERSION = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('system'),
            Choice(0, 
                Terminal('help'),
                NonTerminal('version')
            )
        )
    )
)

system = {
    'system-version': SYSTEM_VERSION
 }
