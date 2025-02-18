import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'FlowOfFunds': 1.0
        })
    )
