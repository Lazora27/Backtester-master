import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'KeltnerChannels': 1.0
        })
    )
