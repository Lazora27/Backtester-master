import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
