import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
