import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
