import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
