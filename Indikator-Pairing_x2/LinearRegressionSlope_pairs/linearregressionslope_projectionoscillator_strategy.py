import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
