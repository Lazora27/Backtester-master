import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und GannFans
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'GannFans': 1.0
        })
    )
