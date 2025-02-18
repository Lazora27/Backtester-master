import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
