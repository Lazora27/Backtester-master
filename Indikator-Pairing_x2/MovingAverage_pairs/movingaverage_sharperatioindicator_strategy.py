import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
