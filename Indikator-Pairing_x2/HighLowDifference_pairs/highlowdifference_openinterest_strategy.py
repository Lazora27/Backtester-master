import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'OpenInterest': 1.0
        })
    )
