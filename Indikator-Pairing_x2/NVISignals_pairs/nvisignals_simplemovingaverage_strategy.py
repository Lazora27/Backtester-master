import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
