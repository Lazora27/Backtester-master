import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
