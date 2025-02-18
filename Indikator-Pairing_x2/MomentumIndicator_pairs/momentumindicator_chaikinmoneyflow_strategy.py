import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_ChaikinMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und ChaikinMoneyFlow
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'ChaikinMoneyFlow': 1.0
        })
    )
