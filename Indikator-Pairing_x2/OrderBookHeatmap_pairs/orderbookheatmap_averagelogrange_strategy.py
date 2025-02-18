import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AverageLogRange': 1.0
        })
    )
