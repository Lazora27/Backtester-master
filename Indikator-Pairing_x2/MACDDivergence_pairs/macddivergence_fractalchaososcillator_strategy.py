import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
