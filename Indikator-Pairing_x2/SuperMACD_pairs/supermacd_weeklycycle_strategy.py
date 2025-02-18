import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WeeklyCycle': 1.0
        })
    )
