import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MassIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MassIndex': 1.0
        })
    )
