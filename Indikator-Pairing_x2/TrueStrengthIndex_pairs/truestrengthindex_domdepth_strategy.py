import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
