import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
