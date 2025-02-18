import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
