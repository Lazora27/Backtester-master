import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'WeeklyCycle': 1.0
        })
    )
