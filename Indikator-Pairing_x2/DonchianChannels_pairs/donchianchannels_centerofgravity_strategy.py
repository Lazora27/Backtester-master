import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'CenterOfGravity': 1.0
        })
    )
