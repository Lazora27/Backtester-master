import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
