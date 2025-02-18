import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
