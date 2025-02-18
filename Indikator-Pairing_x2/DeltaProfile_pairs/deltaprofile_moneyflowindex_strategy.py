import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
