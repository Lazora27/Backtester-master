import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
