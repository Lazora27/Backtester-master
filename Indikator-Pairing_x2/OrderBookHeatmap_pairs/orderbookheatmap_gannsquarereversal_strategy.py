import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'GannSquareReversal': 1.0
        })
    )
