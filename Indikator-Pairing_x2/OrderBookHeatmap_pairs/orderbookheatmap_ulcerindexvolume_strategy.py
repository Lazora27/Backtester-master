import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
