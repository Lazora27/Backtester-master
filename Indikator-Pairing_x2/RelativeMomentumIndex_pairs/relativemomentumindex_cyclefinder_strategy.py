import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
