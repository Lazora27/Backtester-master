import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'IchimokuCloud': 1.0
        })
    )
