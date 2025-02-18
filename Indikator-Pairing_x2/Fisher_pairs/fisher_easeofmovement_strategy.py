import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'EaseOfMovement': 1.0
        })
    )
