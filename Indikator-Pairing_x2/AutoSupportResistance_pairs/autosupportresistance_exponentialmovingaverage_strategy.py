import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
