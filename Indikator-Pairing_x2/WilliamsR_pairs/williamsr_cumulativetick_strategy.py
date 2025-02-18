import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CumulativeTick': 1.0
        })
    )
