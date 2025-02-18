import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
