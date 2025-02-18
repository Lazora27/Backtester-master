import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
