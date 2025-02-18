import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'DonchianChannels': 1.0
        })
    )
