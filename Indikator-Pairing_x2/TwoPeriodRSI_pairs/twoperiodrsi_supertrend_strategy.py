import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
