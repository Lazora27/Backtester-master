import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SmoothedCycle': 1.0
        })
    )
