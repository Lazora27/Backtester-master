import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'KeltnerChannels': 1.0
        })
    )
