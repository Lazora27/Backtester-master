import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
