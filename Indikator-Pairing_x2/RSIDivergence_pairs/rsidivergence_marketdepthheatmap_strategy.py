import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
