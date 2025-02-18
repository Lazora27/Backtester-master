import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
