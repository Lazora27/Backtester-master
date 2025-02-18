import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und CycleFinder
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'CycleFinder': 1.0
        })
    )
