import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
