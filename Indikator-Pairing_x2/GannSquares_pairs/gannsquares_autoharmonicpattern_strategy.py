import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
