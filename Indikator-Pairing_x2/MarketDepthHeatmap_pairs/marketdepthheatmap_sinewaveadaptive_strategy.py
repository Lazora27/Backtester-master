import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
