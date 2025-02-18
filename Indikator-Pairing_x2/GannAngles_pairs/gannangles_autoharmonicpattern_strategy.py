import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
