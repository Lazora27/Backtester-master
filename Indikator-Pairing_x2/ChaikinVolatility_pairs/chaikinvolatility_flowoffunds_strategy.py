import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'FlowOfFunds': 1.0
        })
    )
