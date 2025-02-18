import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
