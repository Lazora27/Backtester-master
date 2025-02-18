import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
