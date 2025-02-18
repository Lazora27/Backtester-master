import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
