import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
