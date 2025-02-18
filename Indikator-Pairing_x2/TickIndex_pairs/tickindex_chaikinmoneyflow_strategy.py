import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ChaikinMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ChaikinMoneyFlow
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ChaikinMoneyFlow': 1.0
        })
    )
