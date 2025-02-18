import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
