import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
