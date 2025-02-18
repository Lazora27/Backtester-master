import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
