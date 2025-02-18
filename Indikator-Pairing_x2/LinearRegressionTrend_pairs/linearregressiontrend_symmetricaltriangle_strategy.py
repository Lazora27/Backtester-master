import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
