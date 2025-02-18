import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'DonchianChannels': 1.0
        })
    )
