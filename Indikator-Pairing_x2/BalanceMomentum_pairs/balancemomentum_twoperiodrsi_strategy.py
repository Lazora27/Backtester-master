import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
