import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'AroonIndicator': 1.0
        })
    )
