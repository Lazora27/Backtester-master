import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AccelerationBands': 1.0
        })
    )
