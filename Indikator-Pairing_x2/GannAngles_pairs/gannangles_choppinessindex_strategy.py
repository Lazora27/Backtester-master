import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
