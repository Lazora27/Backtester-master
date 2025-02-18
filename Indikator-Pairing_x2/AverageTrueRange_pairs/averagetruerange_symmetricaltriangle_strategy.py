import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
