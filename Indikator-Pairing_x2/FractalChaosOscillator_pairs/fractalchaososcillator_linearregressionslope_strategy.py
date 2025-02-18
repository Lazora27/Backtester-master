import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
