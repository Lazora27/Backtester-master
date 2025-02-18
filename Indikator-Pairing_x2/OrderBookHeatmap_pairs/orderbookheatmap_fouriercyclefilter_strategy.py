import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
