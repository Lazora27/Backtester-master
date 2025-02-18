import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
