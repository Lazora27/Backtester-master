import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
