import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
