import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TimeCycle': 1.0
        })
    )
