import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
