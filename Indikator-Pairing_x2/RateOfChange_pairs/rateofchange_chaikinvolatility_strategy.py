import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
