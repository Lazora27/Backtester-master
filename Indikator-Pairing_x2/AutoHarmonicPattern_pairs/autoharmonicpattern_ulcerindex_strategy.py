import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'UlcerIndex': 1.0
        })
    )
