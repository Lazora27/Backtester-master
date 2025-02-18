import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'CenterOfGravity': 1.0
        })
    )
