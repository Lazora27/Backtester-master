import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
