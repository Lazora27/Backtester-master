import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
