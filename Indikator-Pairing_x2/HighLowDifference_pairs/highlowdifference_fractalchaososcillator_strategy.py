import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
