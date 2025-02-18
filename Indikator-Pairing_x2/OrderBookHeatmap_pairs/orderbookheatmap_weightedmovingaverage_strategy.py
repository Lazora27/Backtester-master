import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
