import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
