import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
