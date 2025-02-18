import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AAIISentiment': 1.0
        })
    )
