import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'TimeCycle': 1.0
        })
    )
