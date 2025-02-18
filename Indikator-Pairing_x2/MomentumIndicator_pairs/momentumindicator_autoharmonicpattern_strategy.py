import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
