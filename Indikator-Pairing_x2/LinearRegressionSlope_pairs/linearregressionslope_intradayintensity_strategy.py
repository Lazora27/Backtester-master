import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'IntradayIntensity': 1.0
        })
    )
