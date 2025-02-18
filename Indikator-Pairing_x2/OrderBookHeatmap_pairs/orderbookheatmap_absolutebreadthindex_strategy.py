import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
