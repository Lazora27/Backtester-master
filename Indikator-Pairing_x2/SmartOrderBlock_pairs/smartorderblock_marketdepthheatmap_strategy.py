import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
