import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
