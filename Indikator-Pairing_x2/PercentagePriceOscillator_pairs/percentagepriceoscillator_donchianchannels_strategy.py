import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'DonchianChannels': 1.0
        })
    )
