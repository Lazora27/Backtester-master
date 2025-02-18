import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
