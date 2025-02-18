import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ShortTermVolatilityIndex_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ShortTermVolatilityIndex und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'ShortTermVolatilityIndex': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
