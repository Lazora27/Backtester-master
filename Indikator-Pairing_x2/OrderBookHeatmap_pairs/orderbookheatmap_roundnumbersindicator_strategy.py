import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
