import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
