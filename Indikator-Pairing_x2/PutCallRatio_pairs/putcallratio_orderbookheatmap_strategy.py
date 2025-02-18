import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
