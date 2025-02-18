import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HilbertSinewave': 1.0
        })
    )
