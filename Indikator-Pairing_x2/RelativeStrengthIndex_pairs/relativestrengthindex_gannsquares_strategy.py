import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'GannSquares': 1.0
        })
    )
