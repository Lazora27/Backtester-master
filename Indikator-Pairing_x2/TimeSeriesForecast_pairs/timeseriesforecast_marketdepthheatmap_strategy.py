import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
