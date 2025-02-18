import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
