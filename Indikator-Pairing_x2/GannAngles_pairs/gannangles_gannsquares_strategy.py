import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und GannSquares
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'GannSquares': 1.0
        })
    )
