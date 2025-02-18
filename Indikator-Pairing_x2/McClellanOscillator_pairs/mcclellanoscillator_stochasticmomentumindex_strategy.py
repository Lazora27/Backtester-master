import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
