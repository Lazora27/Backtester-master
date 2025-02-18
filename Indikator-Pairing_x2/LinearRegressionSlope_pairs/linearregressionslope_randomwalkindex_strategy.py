import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
