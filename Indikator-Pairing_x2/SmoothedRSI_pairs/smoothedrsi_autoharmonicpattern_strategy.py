import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
