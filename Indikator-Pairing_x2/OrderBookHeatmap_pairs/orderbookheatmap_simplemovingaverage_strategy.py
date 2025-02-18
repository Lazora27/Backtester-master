import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
