import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
