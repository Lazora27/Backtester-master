import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'AdaptiveATR': 1.0
        })
    )
