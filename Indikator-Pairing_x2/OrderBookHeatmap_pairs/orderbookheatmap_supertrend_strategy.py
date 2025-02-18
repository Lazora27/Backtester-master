import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SuperTrend
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SuperTrend': 1.0
        })
    )
