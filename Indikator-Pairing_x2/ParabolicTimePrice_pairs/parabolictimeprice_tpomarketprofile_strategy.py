import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
