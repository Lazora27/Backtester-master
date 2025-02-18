import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
