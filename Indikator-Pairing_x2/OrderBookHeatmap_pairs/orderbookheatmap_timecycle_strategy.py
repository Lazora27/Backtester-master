import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TimeCycle
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TimeCycle': 1.0
        })
    )
