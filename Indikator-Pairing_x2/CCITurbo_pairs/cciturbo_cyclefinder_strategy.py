import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'CycleFinder': 1.0
        })
    )
