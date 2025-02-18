import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
