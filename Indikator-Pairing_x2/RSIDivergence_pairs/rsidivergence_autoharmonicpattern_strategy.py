import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
