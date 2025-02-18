import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'FibonacciZones': 1.0
        })
    )
