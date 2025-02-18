import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
