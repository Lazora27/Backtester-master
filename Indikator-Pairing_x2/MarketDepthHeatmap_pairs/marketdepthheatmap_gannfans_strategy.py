import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und GannFans
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'GannFans': 1.0
        })
    )
