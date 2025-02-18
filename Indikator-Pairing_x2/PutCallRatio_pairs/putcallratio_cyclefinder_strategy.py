import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CycleFinder': 1.0
        })
    )
