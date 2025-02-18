import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'OpenInterest': 1.0
        })
    )
