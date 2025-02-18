import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
