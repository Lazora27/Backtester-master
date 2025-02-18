import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
