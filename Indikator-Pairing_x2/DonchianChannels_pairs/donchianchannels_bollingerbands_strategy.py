import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BollingerBands
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BollingerBands': 1.0
        })
    )
