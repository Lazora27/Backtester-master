import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
