import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
