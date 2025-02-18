import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
