import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
