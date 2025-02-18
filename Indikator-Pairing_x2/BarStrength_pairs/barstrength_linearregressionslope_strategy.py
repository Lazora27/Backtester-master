import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
