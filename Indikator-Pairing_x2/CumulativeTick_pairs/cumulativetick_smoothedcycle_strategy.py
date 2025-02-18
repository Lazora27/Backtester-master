import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SmoothedCycle': 1.0
        })
    )
