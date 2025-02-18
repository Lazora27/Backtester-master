import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
