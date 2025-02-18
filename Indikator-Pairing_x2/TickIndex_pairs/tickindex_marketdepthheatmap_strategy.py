import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
