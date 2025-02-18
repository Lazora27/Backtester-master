import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und TrendCycles
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'TrendCycles': 1.0
        })
    )
