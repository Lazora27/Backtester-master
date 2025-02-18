import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
