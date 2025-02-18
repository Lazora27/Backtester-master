import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
