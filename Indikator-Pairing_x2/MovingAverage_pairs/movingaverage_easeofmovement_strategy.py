import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'EaseOfMovement': 1.0
        })
    )
