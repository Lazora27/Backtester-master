import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
