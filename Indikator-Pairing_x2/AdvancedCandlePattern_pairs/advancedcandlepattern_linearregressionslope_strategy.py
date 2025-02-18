import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
