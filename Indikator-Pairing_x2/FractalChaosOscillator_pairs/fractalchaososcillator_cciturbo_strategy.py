import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
