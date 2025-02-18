import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
