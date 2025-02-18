import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AverageLogRange': 1.0
        })
    )
