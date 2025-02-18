import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HilbertTrendline': 1.0
        })
    )
