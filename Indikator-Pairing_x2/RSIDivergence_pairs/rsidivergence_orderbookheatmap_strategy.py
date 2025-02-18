import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
