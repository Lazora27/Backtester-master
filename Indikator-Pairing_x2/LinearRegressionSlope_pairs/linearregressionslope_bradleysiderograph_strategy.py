import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'BradleySiderograph': 1.0
        })
    )
