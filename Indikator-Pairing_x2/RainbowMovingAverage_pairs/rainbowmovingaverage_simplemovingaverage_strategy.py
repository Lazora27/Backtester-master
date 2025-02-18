import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
