import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CumulativeTick': 1.0
        })
    )
