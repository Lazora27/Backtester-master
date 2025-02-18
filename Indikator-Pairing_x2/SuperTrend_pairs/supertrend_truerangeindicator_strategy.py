import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
