import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
