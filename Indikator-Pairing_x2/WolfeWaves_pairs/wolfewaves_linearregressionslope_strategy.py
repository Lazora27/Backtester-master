import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
