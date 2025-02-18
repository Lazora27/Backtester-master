import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
