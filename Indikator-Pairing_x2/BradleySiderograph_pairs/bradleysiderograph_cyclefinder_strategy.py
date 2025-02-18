import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'CycleFinder': 1.0
        })
    )
