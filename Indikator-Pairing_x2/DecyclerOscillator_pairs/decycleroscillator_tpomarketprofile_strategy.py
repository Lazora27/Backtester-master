import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
