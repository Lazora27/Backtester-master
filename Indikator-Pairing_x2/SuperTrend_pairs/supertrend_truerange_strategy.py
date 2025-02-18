import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TrueRange
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TrueRange': 1.0
        })
    )
