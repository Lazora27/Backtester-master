import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
