import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
