import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'GannSquares': 1.0
        })
    )
