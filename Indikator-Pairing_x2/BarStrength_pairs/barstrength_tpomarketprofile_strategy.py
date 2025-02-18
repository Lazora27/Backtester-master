import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
