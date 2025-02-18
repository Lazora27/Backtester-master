import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
