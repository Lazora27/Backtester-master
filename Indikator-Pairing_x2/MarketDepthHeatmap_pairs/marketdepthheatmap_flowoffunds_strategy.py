import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'FlowOfFunds': 1.0
        })
    )
