import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TimeCycle': 1.0
        })
    )
