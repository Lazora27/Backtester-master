import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'ProjectionBands': 1.0
        })
    )
