import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
