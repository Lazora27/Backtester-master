import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
