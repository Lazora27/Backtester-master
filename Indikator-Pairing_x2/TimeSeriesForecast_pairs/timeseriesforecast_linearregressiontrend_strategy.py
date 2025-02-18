import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
