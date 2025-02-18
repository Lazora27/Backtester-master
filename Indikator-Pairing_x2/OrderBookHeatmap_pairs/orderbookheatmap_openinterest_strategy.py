import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und OpenInterest
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'OpenInterest': 1.0
        })
    )
