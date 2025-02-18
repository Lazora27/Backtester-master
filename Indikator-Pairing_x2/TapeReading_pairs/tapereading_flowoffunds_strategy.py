import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FlowOfFunds': 1.0
        })
    )
