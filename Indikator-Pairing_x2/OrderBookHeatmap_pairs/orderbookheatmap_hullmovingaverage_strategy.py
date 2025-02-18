import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HullMovingAverage': 1.0
        })
    )
