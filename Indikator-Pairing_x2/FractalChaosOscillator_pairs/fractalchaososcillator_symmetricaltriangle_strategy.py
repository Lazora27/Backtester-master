import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
