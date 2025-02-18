import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
