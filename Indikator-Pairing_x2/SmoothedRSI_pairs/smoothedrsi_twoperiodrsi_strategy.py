import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
