import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
