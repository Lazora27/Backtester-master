import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
