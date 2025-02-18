import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
