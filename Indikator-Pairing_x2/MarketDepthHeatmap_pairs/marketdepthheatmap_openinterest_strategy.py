import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'OpenInterest': 1.0
        })
    )
