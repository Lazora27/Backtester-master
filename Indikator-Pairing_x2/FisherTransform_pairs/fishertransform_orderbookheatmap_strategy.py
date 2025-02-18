import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
