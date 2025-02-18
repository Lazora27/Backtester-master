import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
