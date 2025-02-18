import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und BarStrength
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'BarStrength': 1.0
        })
    )
