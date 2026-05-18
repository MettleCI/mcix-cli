import cairosvg
from railroad import *

CLI_COMMAND_MODE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('{namespace}'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('{command}'), 
                    Choice(0,
                        'help',
                            Skip(),
                            MultipleChoice(0, 'any',
                                NonTerminal('-option'),
                                Sequence(NonTerminal('-option'), '{value}')
                            )
                    )
                    )
                )
            )
        )
    )


misc = {
    'cli-command-mode': CLI_COMMAND_MODE
}