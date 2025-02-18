import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PriceSquawk': 1.0
        })
    )
