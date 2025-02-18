import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AdaptiveATR': 1.0
        })
    )
