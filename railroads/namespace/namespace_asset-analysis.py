import cairosvg
from railroad import *

ASSET_ANALYSIS_QUERY = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('asset-analysis'),
            NonTerminal('query')
        ), 
        Choice(0,
            Sequence(
                MultipleChoice(0, 'all',
                    Sequence(NonTerminal('-queries'), '{location of query files}'),
                    Sequence(NonTerminal('-assets'), '{location of ISX assets}'),
                    Sequence(NonTerminal('-report'), '{CSV output report name}')
                ),
                Optional( 
                    Sequence(NonTerminal('-threads'), '{number of execution threads}')
                )
            )
        )
    )
)

ASSET_ANALYSIS_TEST = Diagram(
    Stack(
        Sequence(
            NonTerminal('mcix'),
            NonTerminal('asset-analysis'),
            NonTerminal('test')
        ),
        Choice(0,
            MultipleChoice(0, 'all',
                Sequence(NonTerminal('-rules'), '{location of compliance rules}'),
                Sequence(NonTerminal('-assets'), '{location of ISX assets}'),
                Sequence(NonTerminal('-report'), '{xml output report name}')                        
            ),
            MultipleChoice(0, 'any',
                Sequence(Skip()), 
                Sequence(NonTerminal('-junit')),
                Sequence(NonTerminal('-include-tag'), '{list of tags}'),
                Sequence(NonTerminal('-exclude-tag'), '{list of tags}'),
                Sequence(NonTerminal('-project-cache'), '{number of execution threads}'),
                Sequence(NonTerminal('-test-suite'), '{test suite label}'),
                Sequence(NonTerminal('-ignore-test-failures')),
                Sequence(NonTerminal('-include-job-in-test-name'))
            )
        )
    )
)

compliance = {
    'asset-analysis-query': ASSET_ANALYSIS_QUERY,
    'asset-analysis-test': ASSET_ANALYSIS_TEST
}
