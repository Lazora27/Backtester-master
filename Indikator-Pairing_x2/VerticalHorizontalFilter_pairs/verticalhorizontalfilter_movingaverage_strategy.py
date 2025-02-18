import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und MovingAverage
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'MovingAverage': 1.0
        })
    )
