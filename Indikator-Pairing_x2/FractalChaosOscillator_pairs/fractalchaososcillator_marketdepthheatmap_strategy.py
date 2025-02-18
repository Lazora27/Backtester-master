import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
