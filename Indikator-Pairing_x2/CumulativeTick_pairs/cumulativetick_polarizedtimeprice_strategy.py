import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
