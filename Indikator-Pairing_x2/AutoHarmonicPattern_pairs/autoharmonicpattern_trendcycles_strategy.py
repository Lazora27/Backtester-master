import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'TrendCycles': 1.0
        })
    )
