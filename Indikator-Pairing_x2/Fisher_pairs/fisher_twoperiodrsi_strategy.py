import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
