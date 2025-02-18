import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
