import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PriceSquawk': 1.0
        })
    )
