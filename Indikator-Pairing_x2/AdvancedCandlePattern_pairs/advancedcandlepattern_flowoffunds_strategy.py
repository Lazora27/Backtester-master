import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'FlowOfFunds': 1.0
        })
    )
