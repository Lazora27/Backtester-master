import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
