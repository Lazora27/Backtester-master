import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'CCITurbo': 1.0
        })
    )
