import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MassIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MassIndex': 1.0
        })
    )
