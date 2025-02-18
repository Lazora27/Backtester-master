import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
