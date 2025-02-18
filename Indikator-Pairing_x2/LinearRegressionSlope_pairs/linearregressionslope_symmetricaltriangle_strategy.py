import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
