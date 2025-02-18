import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FlowOfFunds': 1.0
        })
    )
