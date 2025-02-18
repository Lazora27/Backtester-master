import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
