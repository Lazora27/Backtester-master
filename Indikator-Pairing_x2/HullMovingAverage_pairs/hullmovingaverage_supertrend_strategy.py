import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und SuperTrend
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'SuperTrend': 1.0
        })
    )
