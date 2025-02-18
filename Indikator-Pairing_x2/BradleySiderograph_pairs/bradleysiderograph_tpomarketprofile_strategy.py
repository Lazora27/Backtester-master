import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
