import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und CycleFinder
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'CycleFinder': 1.0
        })
    )
