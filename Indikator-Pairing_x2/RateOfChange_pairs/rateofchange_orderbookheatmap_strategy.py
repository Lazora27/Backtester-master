import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
