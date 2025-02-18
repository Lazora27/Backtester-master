import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
