import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
