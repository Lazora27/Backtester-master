import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und CycleFinder
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'CycleFinder': 1.0
        })
    )
