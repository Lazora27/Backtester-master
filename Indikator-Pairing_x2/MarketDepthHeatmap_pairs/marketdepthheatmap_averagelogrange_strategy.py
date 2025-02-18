import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'AverageLogRange': 1.0
        })
    )
