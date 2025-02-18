import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SuperTrend
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SuperTrend': 1.0
        })
    )
