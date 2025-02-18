import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
