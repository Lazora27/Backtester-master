import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
