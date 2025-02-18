import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
