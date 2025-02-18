import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
