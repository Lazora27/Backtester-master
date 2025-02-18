import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'CCITurbo': 1.0
        })
    )
