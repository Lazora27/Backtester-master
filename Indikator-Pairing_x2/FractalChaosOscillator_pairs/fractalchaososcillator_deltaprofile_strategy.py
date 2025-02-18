import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
