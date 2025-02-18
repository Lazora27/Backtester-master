import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
