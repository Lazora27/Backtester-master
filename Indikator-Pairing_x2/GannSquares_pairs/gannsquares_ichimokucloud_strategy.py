import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'IchimokuCloud': 1.0
        })
    )
