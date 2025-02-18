import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ModifiedATR': 1.0
        })
    )
