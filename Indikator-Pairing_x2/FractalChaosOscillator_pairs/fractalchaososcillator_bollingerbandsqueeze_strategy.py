import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
