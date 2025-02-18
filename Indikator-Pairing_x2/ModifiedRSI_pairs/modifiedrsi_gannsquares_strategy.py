import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'GannSquares': 1.0
        })
    )
