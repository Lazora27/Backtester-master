import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
