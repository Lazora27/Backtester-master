import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'CycleFinder': 1.0
        })
    )
