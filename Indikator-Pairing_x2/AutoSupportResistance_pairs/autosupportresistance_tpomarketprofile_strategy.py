import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
