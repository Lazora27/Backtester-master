import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
