import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
