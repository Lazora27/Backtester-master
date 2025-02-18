import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
