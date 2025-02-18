import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'ProjectionBands': 1.0
        })
    )
