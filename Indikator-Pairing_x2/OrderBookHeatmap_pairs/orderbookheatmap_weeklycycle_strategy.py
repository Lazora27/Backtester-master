import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'WeeklyCycle': 1.0
        })
    )
