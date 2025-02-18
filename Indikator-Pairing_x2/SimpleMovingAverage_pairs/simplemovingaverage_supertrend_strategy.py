import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SuperTrend
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SuperTrend': 1.0
        })
    )
