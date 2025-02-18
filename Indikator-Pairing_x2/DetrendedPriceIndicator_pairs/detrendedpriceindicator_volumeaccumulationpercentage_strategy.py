import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceIndicator_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceIndicator und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'DetrendedPriceIndicator': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
