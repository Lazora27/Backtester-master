import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
