import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HilbertTrendline': 1.0
        })
    )
