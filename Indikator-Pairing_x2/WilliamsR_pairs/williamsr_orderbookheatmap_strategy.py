import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
