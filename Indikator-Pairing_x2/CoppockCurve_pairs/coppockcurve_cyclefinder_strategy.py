import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'CycleFinder': 1.0
        })
    )
