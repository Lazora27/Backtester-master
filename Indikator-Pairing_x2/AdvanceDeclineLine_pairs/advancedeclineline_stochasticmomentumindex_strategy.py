import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
