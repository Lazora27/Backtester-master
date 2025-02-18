import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'GannAngles': 1.0
        })
    )
