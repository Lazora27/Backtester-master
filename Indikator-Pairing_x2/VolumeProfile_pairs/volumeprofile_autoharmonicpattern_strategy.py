import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
