import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
