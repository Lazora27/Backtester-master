import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'WeightedCycle': 1.0
        })
    )
