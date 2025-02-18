import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
