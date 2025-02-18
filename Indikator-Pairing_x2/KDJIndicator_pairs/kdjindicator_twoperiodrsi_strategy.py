import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
