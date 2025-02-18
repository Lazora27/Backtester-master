import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
