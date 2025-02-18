import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
