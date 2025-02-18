import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'ModifiedATR': 1.0
        })
    )
