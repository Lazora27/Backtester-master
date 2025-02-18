import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
