import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'EaseOfMovement': 1.0
        })
    )
