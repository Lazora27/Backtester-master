import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
