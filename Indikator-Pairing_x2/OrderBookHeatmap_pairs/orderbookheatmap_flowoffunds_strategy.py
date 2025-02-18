import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FlowOfFunds': 1.0
        })
    )
