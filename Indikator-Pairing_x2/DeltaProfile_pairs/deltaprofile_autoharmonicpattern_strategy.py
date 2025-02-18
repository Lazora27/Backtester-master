import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
