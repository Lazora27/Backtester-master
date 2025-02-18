import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
