import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WeeklyCycle': 1.0
        })
    )
