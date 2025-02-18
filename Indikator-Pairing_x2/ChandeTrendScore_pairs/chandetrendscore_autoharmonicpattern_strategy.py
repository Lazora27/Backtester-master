import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
