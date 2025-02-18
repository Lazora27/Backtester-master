import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
