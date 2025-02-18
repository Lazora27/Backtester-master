import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolumeProfile': 1.0
        })
    )
