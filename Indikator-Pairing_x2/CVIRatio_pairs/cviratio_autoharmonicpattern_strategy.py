import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
