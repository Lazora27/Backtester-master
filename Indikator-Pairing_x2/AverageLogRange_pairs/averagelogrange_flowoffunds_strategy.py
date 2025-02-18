import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'FlowOfFunds': 1.0
        })
    )
