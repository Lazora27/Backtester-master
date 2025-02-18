import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'GannSquares': 1.0
        })
    )
