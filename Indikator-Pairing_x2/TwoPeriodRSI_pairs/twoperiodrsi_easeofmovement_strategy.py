import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'EaseOfMovement': 1.0
        })
    )
