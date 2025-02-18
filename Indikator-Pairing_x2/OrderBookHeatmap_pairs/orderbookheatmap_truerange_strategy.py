import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TrueRange
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TrueRange': 1.0
        })
    )
