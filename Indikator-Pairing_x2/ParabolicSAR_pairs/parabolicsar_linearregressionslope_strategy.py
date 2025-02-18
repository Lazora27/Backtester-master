import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
