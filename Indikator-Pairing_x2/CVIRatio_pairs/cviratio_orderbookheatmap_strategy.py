import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
