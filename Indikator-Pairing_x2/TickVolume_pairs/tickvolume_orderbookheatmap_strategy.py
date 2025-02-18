import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
