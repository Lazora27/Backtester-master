import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
