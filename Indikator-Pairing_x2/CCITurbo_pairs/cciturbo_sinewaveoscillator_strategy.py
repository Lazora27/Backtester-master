import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
