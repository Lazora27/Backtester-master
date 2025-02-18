import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CycleFinder
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CycleFinder': 1.0
        })
    )
