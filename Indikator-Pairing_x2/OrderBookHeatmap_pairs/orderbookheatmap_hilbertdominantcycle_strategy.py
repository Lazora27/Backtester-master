import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
