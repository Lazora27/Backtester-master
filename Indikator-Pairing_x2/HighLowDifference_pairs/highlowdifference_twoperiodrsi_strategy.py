import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
