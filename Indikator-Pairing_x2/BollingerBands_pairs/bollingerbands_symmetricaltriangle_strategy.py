import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
