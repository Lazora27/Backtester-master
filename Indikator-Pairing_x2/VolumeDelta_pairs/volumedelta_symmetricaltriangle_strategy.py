import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
