import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
