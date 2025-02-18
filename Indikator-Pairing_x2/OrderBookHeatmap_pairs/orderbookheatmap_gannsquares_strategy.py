import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und GannSquares
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'GannSquares': 1.0
        })
    )
