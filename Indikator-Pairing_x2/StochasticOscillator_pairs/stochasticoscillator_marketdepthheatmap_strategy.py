import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
