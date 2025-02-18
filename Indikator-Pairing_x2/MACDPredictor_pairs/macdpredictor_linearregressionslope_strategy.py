import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
