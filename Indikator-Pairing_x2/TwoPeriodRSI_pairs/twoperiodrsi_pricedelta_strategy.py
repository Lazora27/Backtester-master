import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
