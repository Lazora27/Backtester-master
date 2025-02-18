import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
