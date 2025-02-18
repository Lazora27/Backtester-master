import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
