import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
