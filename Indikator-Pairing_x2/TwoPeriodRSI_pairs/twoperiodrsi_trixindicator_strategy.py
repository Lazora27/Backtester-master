import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TRIXIndicator': 1.0
        })
    )
