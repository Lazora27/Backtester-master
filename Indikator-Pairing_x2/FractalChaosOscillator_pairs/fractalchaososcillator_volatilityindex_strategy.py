import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'VolatilityIndex': 1.0
        })
    )
