import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
