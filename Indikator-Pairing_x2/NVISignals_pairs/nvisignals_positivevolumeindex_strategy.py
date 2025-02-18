import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
