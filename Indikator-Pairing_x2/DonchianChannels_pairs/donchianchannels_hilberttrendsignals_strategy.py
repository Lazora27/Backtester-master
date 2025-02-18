import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
