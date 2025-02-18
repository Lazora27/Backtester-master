import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
