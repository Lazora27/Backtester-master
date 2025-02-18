import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
