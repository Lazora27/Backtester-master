import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
