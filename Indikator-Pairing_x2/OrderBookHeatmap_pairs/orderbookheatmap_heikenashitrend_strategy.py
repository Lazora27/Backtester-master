import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
