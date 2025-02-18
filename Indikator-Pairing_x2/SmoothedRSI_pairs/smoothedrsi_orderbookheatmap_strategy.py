import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
