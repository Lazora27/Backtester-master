import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
