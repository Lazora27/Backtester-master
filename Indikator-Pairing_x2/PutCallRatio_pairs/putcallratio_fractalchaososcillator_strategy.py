import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
