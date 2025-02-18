import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ModifiedATR': 1.0
        })
    )
