import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
