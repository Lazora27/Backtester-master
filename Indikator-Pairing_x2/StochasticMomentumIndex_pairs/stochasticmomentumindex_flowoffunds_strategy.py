import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
