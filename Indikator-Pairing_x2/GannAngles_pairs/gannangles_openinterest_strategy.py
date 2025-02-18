import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und OpenInterest
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'OpenInterest': 1.0
        })
    )
