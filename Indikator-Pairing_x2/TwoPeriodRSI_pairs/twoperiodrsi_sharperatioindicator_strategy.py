import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
