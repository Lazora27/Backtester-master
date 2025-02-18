import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
