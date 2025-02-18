import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
