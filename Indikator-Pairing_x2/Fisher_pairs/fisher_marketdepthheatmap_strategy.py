import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
