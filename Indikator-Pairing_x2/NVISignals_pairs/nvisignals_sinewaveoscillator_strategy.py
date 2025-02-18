import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
