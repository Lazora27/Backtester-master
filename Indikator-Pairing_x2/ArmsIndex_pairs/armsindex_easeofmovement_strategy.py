import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
