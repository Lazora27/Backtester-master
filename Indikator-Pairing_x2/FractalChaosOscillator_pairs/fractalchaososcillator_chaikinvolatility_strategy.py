import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
