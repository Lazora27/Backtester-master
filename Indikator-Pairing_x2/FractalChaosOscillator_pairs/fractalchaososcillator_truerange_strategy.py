import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
