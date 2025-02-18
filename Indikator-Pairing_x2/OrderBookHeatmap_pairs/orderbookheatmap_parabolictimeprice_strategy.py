import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
