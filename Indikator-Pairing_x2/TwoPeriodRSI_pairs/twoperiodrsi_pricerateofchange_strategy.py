import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
