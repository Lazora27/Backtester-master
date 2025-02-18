import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CycleFinder': 1.0
        })
    )
