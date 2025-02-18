import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'EaseOfMovement': 1.0
        })
    )
