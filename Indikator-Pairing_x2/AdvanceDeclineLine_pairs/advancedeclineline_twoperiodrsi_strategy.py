import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
