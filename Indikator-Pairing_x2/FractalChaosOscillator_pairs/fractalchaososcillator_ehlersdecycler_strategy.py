import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
