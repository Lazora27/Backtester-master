import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
