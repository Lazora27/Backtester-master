import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
