import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
