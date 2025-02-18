import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
