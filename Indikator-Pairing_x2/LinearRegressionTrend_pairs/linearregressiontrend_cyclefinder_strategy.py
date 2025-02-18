import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und CycleFinder
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'CycleFinder': 1.0
        })
    )
