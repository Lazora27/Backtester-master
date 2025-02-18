import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
