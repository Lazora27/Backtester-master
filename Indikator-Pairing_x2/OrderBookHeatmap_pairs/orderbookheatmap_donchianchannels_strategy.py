import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DonchianChannels': 1.0
        })
    )
