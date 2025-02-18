import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WeeklyCycle': 1.0
        })
    )
