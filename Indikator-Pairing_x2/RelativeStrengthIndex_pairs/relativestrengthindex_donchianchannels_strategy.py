import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
