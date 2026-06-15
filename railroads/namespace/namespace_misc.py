import cairosvg
from railroad import *

CLI_COMMAND_MODE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        Sequence(
            Terminal('help')
        ),
        Sequence(
            Terminal('help'),
            NonTerminal('{namespace}')
        ),
        Sequence(
            Terminal('help'),
            NonTerminal('{namespace}'),
            NonTerminal('{command}')
        ),
        Sequence(
            NonTerminal('{namespace}'),
            Choice(0, 
                Sequence(
                    NonTerminal('{command}'), 
                    Choice(0,
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