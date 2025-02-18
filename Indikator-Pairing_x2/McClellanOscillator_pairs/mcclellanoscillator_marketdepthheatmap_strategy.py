import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
