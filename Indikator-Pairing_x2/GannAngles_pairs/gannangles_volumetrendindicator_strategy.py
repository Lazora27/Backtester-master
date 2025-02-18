import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
