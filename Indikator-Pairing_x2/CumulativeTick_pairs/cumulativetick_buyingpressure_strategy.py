import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BuyingPressure': 1.0
        })
    )
