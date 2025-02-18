import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
