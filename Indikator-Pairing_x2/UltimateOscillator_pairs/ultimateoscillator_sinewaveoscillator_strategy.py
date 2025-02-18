import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
