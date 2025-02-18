import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
