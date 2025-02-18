import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
