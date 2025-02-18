import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und MassIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'MassIndex': 1.0
        })
    )
