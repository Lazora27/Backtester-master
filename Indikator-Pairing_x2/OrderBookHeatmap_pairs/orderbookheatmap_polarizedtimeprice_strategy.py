import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
