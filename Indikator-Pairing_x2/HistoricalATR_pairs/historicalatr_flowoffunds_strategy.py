import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'FlowOfFunds': 1.0
        })
    )
