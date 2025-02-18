import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
