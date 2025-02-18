import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
