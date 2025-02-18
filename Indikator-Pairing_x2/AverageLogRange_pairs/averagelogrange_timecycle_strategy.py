import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'TimeCycle': 1.0
        })
    )
