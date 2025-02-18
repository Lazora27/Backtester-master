import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
