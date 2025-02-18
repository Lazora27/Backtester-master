import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'PhaseDivergence': 1.0
        })
    )
