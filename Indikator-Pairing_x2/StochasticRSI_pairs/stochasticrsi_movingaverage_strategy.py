import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MovingAverage': 1.0
        })
    )
