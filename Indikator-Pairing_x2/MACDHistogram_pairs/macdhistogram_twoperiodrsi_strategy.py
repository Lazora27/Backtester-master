import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
