import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
