import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
