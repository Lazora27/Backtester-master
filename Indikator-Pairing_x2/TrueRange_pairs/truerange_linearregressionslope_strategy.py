import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
