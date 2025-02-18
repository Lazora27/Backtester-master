import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
