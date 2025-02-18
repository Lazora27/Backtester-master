import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'EaseOfMovement': 1.0
        })
    )
