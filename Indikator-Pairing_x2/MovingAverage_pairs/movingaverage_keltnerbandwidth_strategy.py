import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
