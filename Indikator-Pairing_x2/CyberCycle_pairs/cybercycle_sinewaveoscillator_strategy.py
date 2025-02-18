import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
