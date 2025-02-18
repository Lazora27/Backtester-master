import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
