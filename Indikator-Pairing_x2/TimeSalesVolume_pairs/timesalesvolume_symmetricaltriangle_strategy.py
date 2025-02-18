import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
