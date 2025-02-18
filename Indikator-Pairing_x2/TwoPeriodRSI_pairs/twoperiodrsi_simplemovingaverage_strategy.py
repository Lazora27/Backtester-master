import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
