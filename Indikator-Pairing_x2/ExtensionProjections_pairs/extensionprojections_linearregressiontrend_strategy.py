import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
