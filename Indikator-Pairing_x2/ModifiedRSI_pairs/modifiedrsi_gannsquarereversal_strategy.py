import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
