import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
