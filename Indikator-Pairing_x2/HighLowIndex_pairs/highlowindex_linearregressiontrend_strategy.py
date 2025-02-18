import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
