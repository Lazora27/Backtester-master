import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
