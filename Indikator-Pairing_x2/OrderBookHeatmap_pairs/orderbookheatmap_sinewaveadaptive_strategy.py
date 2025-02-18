import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
