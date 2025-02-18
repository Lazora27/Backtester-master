import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
