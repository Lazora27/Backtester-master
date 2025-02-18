import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'GannSquareReversal': 1.0
        })
    )
