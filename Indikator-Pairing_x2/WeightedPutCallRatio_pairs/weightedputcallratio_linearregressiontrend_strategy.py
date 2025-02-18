import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
