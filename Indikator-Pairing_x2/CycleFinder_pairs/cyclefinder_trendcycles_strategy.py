import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'TrendCycles': 1.0
        })
    )
