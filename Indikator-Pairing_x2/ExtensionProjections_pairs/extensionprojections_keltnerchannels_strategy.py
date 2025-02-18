import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'KeltnerChannels': 1.0
        })
    )
