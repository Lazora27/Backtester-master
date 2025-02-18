import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
