import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TickActivityIndex': 1.0
        })
    )
