import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
