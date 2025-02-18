import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FlowOfFunds': 1.0
        })
    )
