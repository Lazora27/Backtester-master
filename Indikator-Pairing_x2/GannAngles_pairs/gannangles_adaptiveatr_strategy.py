import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AdaptiveATR': 1.0
        })
    )
