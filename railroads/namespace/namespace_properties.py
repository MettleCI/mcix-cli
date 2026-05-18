import cairosvg
from railroad import *

PROPERTIES_CONFIG = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('properties'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('config'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-baseDir'), '{filename}'),
                                Sequence(NonTerminal('-properties'), '{filename}'),
                                Sequence(NonTerminal('-outDir'), '{directory}'),
                            ),
                             Optional(NonTerminal('-filePattern'))
                        )
                    )
                )
            )
        )
    )
)

properties = {
    'properties_config': PROPERTIES_CONFIG
}