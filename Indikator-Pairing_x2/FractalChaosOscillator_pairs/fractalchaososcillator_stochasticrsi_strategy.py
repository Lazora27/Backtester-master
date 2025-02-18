import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
