import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'FlowOfFunds': 1.0
        })
    )
