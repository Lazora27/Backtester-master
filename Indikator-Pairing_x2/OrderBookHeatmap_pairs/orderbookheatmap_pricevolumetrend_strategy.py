import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
