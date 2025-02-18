import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
