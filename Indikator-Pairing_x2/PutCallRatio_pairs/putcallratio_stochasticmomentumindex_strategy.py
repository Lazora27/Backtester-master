import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
