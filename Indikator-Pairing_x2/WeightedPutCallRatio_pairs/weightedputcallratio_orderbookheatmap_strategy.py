import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
