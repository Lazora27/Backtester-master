import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
