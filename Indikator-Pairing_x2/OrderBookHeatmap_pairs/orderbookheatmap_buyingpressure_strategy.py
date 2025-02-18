import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BuyingPressure': 1.0
        })
    )
