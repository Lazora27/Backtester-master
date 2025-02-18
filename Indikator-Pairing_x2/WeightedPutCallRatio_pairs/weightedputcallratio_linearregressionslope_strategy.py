import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
