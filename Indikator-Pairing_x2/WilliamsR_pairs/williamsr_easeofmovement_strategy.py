import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'EaseOfMovement': 1.0
        })
    )
