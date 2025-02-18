import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
