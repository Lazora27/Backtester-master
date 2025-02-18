import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
