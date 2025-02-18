import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'WeightedCycle': 1.0
        })
    )
