import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
