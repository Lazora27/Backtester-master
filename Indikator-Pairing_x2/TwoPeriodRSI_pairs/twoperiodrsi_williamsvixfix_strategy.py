import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
