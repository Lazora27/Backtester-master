import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
