import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'TimeCycle': 1.0
        })
    )
