import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'TimeCycle': 1.0
        })
    )
