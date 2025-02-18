import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
