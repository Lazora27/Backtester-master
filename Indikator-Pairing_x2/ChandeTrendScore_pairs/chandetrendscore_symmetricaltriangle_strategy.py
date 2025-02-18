import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
