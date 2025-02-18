import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
