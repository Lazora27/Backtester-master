import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DonchianChannels': 1.0
        })
    )
