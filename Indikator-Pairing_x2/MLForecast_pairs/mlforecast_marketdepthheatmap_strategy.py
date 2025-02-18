import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
