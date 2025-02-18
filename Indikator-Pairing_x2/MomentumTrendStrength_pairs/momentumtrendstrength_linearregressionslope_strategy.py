import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
