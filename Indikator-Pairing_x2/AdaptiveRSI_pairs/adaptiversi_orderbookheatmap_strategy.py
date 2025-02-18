import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
