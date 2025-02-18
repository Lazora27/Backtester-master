import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'KeltnerChannels': 1.0
        })
    )
