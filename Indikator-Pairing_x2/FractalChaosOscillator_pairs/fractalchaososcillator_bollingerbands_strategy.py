import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
