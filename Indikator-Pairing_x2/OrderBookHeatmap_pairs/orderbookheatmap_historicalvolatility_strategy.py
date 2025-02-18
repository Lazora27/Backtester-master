import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
