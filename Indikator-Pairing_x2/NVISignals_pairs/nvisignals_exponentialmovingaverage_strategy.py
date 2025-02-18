import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
