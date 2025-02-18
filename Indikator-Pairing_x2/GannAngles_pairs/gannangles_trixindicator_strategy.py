import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TRIXIndicator': 1.0
        })
    )
