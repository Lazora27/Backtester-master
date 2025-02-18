import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
