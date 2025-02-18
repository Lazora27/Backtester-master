import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
