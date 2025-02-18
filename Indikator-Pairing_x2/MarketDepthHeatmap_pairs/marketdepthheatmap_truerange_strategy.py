import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und TrueRange
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'TrueRange': 1.0
        })
    )
