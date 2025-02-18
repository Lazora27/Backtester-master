import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AutoFibonacci': 1.0
        })
    )
