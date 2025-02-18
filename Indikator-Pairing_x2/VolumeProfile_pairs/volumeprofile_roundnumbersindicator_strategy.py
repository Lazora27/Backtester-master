import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
