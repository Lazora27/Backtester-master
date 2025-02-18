import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MACDHistogram': 1.0
        })
    )
