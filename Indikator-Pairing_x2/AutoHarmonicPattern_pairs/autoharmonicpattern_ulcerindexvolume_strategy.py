import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
