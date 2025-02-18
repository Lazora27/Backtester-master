import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
