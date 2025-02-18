import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'WilliamsR': 1.0
        })
    )
