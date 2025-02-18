import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
