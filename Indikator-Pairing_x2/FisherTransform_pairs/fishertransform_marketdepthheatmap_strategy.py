import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
