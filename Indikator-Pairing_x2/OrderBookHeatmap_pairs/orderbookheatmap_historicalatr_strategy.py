import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HistoricalATR': 1.0
        })
    )
