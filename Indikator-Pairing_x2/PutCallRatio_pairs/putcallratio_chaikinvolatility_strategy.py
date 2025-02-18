import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
