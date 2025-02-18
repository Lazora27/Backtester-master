import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
