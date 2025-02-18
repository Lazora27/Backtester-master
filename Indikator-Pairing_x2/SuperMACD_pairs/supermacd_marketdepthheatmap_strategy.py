import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
