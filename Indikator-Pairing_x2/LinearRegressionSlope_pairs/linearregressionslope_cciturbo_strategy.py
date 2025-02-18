import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und CCITurbo
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'CCITurbo': 1.0
        })
    )
