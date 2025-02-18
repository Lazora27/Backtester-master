import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
