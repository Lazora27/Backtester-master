import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
