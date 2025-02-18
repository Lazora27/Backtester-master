import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
