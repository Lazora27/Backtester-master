import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HilbertTrendline': 1.0
        })
    )
