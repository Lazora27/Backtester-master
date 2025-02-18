import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und GannAngles
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'GannAngles': 1.0
        })
    )
