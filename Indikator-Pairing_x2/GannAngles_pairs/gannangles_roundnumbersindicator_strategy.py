import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
