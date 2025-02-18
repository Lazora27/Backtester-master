import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DonchianChannels': 1.0
        })
    )
