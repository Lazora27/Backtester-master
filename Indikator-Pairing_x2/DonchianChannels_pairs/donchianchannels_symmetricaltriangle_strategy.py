import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
