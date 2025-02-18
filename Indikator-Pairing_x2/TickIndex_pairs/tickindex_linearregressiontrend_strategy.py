import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
