import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertPhaseIndicator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertPhaseIndicator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HilbertPhaseIndicator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
