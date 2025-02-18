import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'EhlersDecycler': 1.0
        })
    )
