import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'EaseOfMovement': 1.0
        })
    )
