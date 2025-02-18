import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'VolumeOscillator': 1.0
        })
    )
