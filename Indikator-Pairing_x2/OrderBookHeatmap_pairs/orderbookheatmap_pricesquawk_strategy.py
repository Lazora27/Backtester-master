import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PriceSquawk': 1.0
        })
    )
