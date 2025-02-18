import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
