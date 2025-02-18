import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
