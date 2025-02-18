import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
