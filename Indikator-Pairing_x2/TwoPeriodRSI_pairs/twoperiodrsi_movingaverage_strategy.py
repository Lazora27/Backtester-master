import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MovingAverage': 1.0
        })
    )
