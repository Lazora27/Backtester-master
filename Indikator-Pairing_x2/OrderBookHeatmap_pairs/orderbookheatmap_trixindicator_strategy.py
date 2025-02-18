import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TRIXIndicator': 1.0
        })
    )
