import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und GannSquares
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'GannSquares': 1.0
        })
    )
