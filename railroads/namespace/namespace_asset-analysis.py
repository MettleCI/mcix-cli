import cairosvg
from railroad import *

ASSET_ANALYSIS_QUERY = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('asset-analysis'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('query'), 
                    Choice(0,
                        'help',
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
        )
    )
)

ASSET_ANALYSIS_REPORTCARD = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('asset-analysis'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('reportcard'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-zipfile'), '{filename}'),
                                Sequence(NonTerminal('-reportdir'), '{directory}'),
                                Sequence(NonTerminal('-client'), '{client name}'),
                                Sequence(NonTerminal('-email'), '{email}')
                            )
                        )
                    )
                )
            )
        )
    )
)

ASSET_ANALYSIS_TEST = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('asset-analysis'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('test'), 
                    Choice(0,
                        'help',
                        Sequence(
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
            )
        )
    )
)

ASSET_ANALYSIS_CONSOLE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('asset-analysis'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('console'), 
                    Choice(0,
                        'help',
                        Sequence(NonTerminal('-assets'), '{Directory or Zip containing project export}')
                    )
                )
            )
        )
    )
)

ASSET_ANALYSIS_LIST_TAGS = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('asset-analysis'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('list-tags'), 
                    Choice(0,
                        'help',
                        Sequence(
                        Choice(0,
                            Sequence(NonTerminal('-rules'), '{location of compliance rules}'),
                            Sequence(NonTerminal('-queries'), '{location of asset queries}')     
                            ),
                        Optional(
                            Sequence(
                                NonTerminal('-format'),
                                Choice(0,
                                    'tabular',
                                    'csv'
                                    )
                                ),
                            'skip'
                            )
                        ) 
                    )
                )
            )
        )
    )
)

compliance = {
    'asset-analysis-query': ASSET_ANALYSIS_QUERY,
    'asset-analysis-reportcard': ASSET_ANALYSIS_REPORTCARD,
    'asset-analysis-test': ASSET_ANALYSIS_TEST,
    'asset-analysis-console': ASSET_ANALYSIS_CONSOLE,
    'asset-analysis-list-tags': ASSET_ANALYSIS_LIST_TAGS
}
