import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SmoothedCycle': 1.0
        })
    )
