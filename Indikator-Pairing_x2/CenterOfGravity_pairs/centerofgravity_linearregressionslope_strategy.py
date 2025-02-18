import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
