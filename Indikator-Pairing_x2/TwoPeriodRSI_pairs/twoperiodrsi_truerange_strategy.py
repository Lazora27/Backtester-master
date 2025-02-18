import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TrueRange': 1.0
        })
    )
