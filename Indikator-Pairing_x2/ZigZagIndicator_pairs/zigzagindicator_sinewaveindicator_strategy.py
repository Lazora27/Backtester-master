import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
