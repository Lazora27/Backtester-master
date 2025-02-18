import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FlowOfFunds': 1.0
        })
    )
