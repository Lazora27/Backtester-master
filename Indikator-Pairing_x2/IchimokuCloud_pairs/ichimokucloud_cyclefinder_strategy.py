import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und CycleFinder
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'CycleFinder': 1.0
        })
    )
