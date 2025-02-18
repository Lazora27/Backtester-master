import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
