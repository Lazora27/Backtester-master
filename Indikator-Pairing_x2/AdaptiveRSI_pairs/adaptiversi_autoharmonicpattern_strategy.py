import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
