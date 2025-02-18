import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HullMovingAverage': 1.0
        })
    )
