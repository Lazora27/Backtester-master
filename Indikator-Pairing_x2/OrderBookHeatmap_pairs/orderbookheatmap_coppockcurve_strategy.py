import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'CoppockCurve': 1.0
        })
    )
