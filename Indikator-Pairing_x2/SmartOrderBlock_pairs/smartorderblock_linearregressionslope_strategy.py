import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
