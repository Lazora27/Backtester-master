import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
