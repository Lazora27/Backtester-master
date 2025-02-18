import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BollingerPercentB': 1.0
        })
    )
