import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
