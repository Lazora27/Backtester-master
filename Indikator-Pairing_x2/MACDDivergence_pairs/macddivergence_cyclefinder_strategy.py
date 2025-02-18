import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CycleFinder': 1.0
        })
    )
