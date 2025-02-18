import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'MarketBalance': 1.0
        })
    )
