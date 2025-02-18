import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VolumeProfile': 1.0
        })
    )
