import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
