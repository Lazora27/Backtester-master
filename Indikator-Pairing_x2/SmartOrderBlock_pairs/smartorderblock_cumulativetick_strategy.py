import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CumulativeTick': 1.0
        })
    )
