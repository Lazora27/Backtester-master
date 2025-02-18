import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SineWaveOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
