import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TimeCycle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TimeCycle': 1.0
        })
    )
