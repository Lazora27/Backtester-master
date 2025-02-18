import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
