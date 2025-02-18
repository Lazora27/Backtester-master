import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
