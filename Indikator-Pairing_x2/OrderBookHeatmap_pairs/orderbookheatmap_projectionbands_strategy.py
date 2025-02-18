import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ProjectionBands': 1.0
        })
    )
