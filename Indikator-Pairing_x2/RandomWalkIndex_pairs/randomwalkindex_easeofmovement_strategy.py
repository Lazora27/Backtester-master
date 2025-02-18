import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
