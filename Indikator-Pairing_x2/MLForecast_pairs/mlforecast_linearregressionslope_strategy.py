import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
