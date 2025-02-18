import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'GannSquareReversal': 1.0
        })
    )
