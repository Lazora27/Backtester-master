import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
