import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'EaseOfMovement': 1.0
        })
    )
