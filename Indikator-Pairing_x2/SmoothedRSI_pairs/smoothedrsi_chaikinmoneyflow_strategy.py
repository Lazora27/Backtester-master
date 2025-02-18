import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ChaikinMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ChaikinMoneyFlow
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ChaikinMoneyFlow': 1.0
        })
    )
