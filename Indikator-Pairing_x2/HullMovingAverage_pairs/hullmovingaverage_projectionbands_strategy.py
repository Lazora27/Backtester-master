import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ProjectionBands': 1.0
        })
    )
