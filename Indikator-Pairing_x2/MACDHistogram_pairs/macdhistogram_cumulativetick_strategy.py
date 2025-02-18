import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'CumulativeTick': 1.0
        })
    )
