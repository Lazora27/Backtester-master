import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MovingAverage': 1.0
        })
    )
