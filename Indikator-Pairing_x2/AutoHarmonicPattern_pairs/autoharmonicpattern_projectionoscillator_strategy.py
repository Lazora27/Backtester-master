import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
