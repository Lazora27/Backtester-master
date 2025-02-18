import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
