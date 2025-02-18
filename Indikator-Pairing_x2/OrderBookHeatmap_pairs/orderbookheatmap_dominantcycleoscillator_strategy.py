import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
