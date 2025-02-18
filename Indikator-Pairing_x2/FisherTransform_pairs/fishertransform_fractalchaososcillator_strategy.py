import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
