import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AAIISentiment': 1.0
        })
    )
