import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
