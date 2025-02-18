import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
