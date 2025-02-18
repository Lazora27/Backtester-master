import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'IntradayIntensity': 1.0
        })
    )
