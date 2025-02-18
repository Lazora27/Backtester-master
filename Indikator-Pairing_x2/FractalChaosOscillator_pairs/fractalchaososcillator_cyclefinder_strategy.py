import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
