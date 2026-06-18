import cairosvg
from railroad import *

SYSTEM_VERSION = Diagram(
    NonTerminal('mcix'),
    NonTerminal('system'),
    NonTerminal('version')
)

system = {
    'system-version': SYSTEM_VERSION
 }
