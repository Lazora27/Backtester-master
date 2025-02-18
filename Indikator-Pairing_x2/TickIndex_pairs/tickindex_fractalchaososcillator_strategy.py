import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
