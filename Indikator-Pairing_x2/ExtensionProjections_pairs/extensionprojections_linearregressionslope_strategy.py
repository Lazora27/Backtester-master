import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
