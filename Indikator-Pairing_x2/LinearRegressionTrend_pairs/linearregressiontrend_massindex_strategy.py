import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und MassIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'MassIndex': 1.0
        })
    )
