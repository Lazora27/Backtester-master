import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
