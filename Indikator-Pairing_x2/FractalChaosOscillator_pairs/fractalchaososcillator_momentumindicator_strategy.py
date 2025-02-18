import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MomentumIndicator': 1.0
        })
    )
