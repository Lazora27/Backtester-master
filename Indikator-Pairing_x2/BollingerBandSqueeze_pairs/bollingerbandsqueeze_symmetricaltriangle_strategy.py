import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
