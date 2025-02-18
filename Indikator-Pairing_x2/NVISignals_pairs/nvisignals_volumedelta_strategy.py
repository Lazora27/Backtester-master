import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolumeDelta': 1.0
        })
    )
