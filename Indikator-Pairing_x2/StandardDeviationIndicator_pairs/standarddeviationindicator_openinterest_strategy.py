import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
