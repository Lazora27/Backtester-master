import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WeeklyCycle': 1.0
        })
    )
