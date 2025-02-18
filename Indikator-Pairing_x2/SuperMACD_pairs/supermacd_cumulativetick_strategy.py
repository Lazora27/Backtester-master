import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CumulativeTick': 1.0
        })
    )
