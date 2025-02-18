import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
