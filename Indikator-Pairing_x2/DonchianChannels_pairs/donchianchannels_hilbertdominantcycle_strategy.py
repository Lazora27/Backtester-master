import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
