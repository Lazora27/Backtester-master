import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
