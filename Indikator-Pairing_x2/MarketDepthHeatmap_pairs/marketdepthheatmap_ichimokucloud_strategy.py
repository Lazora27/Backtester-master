import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'IchimokuCloud': 1.0
        })
    )
