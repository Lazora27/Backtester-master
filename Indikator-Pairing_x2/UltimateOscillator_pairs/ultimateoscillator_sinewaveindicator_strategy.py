import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
