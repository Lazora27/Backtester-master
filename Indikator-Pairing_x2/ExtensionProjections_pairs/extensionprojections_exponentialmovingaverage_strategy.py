import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
