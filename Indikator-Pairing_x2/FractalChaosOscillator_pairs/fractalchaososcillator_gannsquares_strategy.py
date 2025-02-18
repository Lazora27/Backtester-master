import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
