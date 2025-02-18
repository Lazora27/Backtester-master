import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'GannSquareReversal': 1.0
        })
    )
