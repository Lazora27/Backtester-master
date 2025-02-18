import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und GannSquares
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'GannSquares': 1.0
        })
    )
