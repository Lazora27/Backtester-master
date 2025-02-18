import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
