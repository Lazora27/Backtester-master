import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
