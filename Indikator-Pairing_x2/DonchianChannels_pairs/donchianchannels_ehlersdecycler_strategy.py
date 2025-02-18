import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'EhlersDecycler': 1.0
        })
    )
