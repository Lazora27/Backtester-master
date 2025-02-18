import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
