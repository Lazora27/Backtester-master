import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'EaseOfMovement': 1.0
        })
    )
