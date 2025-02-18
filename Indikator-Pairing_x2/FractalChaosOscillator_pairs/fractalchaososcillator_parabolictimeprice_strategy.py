import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
