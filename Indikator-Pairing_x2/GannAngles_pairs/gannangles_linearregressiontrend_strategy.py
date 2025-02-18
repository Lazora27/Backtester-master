import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
