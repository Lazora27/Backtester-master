import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
