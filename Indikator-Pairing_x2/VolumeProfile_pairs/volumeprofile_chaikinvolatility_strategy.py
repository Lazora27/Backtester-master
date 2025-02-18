import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
