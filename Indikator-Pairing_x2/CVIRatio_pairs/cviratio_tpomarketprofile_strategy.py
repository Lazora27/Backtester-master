import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
