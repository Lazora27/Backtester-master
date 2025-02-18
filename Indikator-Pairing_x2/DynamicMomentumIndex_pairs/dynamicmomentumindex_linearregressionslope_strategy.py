import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
