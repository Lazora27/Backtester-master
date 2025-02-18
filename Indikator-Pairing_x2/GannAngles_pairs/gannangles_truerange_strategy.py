import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TrueRange
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TrueRange': 1.0
        })
    )
