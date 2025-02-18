import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'EaseOfMovement': 1.0
        })
    )
