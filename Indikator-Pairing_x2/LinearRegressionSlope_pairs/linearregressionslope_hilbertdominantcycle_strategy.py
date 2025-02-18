import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
