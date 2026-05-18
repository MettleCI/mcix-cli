import cairosvg
from railroad import *

WORKBENCH_SET_BRANCH = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('workbench'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('set-branch'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-url'), '{workbench-url}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),                       
                                Sequence(NonTerminal('-project'), '{project-name}'),                        
                                Sequence(NonTerminal('-branch'), '{branch-name}')                        
                            )
                        )
                    )
                )
            )
        )
    )
)

workbench = {
    'workbench-set-branch': WORKBENCH_SET_BRANCH
}