import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'AdaptiveATR': 1.0
        })
    )
